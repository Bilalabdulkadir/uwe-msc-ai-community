import TopNav from "../components/TopNav";

export default function HomePage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <section style={{ paddingTop: "2rem" }}>
        <h1>UWE MSc AI Community</h1>
        <p>
          A collaborative platform for AI students, staff, alumni, and research partners.
        </p>
      </section>
    </main>
  );
}
