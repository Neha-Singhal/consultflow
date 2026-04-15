import { useState } from "react";
import API from "../api/api";

function LeadForm({ token }) {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [company, setCompany] = useState("");

  const createLead = async () => {

    await API.post(
      "/leads",
      { name, email, company },
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );

    alert("Lead created!");
  };

  return (
    <div>

      <h3>Add Lead</h3>

      <input
        placeholder="Name"
        onChange={e => setName(e.target.value)}
      />

      <input
        placeholder="Email"
        onChange={e => setEmail(e.target.value)}
      />

      <input
        placeholder="Company"
        onChange={e => setCompany(e.target.value)}
      />

      <button onClick={createLead}>Create Lead</button>

    </div>
  );
}

export default LeadForm;