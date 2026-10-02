import TopNav from "../../components/TopNav";

const resources = [
  { title: "FastAPI Tutorial", type: "Tutorial" },
  { title: "PostgreSQL Basics", type: "Guide" },
  { title: "Applied AI Reading Set", type: "Research" },
];

export default function ResourcesPage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <h1>Resources</h1>
      <ul>
        {resources.map((resource) => (
          <li key={resource.title} style={{ marginBottom: "1rem" }}>
            <strong>{resource.title}</strong> — {resource.type}
          </li>
        ))}
      </ul>
    </main>
  );
}
