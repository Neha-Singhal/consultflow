import LeadForm from "../components/LeadForm";
import LeadList from "../components/LeadList";

function Dashboard({ token }) {

  return (

    <div style={{display:"flex"}}>

      {/* Sidebar */}
      <div style={{
        width:"200px",
        background:"#111",
        color:"white",
        height:"100vh",
        padding:"20px"
      }}>

        <h2>ConsultFlow</h2>

        <p>Dashboard</p>
        <p>Leads</p>
        <p>AI Emails</p>

      </div>


      {/* Main Content */}

      <div style={{padding:"40px", width:"100%"}}>

        <h1>Dashboard</h1>

        <LeadForm token={token}/>

        <LeadList token={token}/>

      </div>

    </div>

  );

}

export default Dashboard;