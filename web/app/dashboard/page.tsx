import TopNav from "../components/TopNav";

const stats = [
  { label: "Projects", value: "14" },
  { label: "Events", value: "6" },
  { label: "Resources", value: "27" },
  { label: "Discussions", value: "42" },
];

export default function DashboardPage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <h1>Dashboard</h1>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, minmax(180px, 1fr))", gap: "1rem", marginTop: "2rem" }}>
        {stats.map((stat) => (
          <div key={stat.label} style={{ border: "1px solid #ddd", borderRadius: 12, padding: "1rem" }}>
            <h3>{stat.label}</h3>
            <p style={{ fontSize: "2rem", margin: 0 }}>{stat.value}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
