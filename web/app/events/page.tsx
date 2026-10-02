import TopNav from "../../components/TopNav";

const events = [
  { title: "AI Careers Panel", date: "2026-10-12", location: "UWE Bristol" },
  { title: "Ethical AI Workshop", date: "2026-10-19", location: "Innovation Lab" },
];

export default function EventsPage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <h1>Upcoming Events</h1>
      <ul>
        {events.map((event) => (
          <li key={event.title} style={{ marginBottom: "1rem" }}>
            <strong>{event.title}</strong> — {event.date} at {event.location}
          </li>
        ))}
      </ul>
    </main>
  );
}
