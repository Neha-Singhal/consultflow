import { useEffect, useState } from "react";
import API from "../api/api";

function LeadList({ token }) {

  const [leads, setLeads] = useState([]);

  const loadLeads = async () => {

    const res = await API.get("/leads/", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    setLeads(res.data);
  };

  const sendEmail = async (id) => {

    await API.post(`/ai/send-email/${id}`, {}, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    alert("AI Email Sent!");
  };

  useEffect(() => {
    loadLeads();
  }, []);

  return (

    <div>

      <h3>Your Leads</h3>

      {leads.map(l => (

        <div key={l.id}>

          {l.name} ({l.company})

          <button onClick={() => sendEmail(l.id)}>
            Send AI Email
          </button>

        </div>

      ))}

    </div>

  );
}

export default LeadList;