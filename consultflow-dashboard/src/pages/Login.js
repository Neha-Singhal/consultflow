import { useState } from "react";
import API from "../api/api";

function Login({ setToken }) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {

    const formData = new FormData();

    formData.append("username", email);
    formData.append("password", password);

    const res = await API.post("/login", formData);

    setToken(res.data.access_token);
  };

  return (
    <div>

      <h2>ConsultFlow Login</h2>

      <input
        placeholder="Email"
        onChange={e => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        onChange={e => setPassword(e.target.value)}
      />

      <button onClick={login}>Login</button>

    </div>
  );
}

export default Login;