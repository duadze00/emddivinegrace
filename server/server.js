const express = require("express");
const cors = require("cors");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const pool = require("./db");
require("dotenv").config({ path: "./server/.env" });

const app = express();

app.use(cors({ origin: "*" }));
app.use(express.json());

/* ================= REGISTER ================= */
app.post("/register", async (req, res) => {
  try {
    const {
      username,
      email,
      password,
      confirmPassword,
      phoneNumber,
      dateOfBirth,
      course,
    } = req.body;

    if (
      !username ||
      !email ||
      !password ||
      !confirmPassword ||
      !phoneNumber ||
      !dateOfBirth ||
      !course
    ) {
      return res.status(400).json({ message: "All fields are required" });
    }

    if (password !== confirmPassword) {
      return res.status(400).json({ message: "Passwords do not match" });
    }

    const existingUser = await pool.query(
      "SELECT * FROM users WHERE email = $1",
      [email],
    );

    if (existingUser.rows.length > 0) {
      return res.status(400).json({ message: "Email already exists" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = await pool.query(
      `INSERT INTO users (username, email, password, phone_number, date_of_birth, course)
       VALUES ($1,$2,$3,$4,$5,$6)
       RETURNING *`,
      [username, email, hashedPassword, phoneNumber, dateOfBirth, course],
    );

    res.status(201).json({
      message: "Registration successful",
      user: newUser.rows[0],
    });
  } catch (error) {
    console.log("FULL ERROR:", error);
    res.status(500).json({ message: "Server Error" });
  }
});

/* ================= LOGIN ================= */
app.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await pool.query("SELECT * FROM users WHERE email = $1", [
      email,
    ]);

    if (user.rows.length === 0) {
      return res.status(400).json({ message: "Invalid email or password" });
    }

    const foundUser = user.rows[0];

    const isMatch = await bcrypt.compare(password, foundUser.password);

    if (!isMatch) {
      return res.status(400).json({ message: "Invalid email or password" });
    }

    const token = jwt.sign(
      {
        id: foundUser.id,
        email: foundUser.email,
        course: foundUser.course,
      },
      process.env.JWT_SECRET,
      { expiresIn: "1h" },
    );

    res.json({
      message: "Login successful",
      token,
      course: foundUser.course,
    });
  } catch (error) {
    console.log("LOGIN ERROR:", error);
    res.status(500).json({ message: "Server error" });
  }
});

/* ================= SERVER START (MUST BE LAST) ================= */

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
