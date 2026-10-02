import TopNav from "../../components/TopNav";

const projects = [
  { title: "Climate Forecasting Dashboard", tech: ["Python", "ML", "Dashboard"] },
  { title: "RAG Research Assistant", tech: ["FastAPI", "LLM", "Search"] },
];

export default function ProjectsPage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <h1>Projects</h1>
      <ul>
        {projects.map((project) => (
          <li key={project.title} style={{ marginBottom: "1rem" }}>
            <strong>{project.title}</strong>
            <div>{project.tech.join(" • ")}</div>
          </li>
        ))}
      </ul>
    </main>
  );
}
