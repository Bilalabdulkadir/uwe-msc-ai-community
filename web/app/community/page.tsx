import TopNav from "../../components/TopNav";

const discussions = [
  { title: "Welcome to the community", author: "Demo Student" },
  { title: "AI project collaborations", author: "Demo Lecturer" },
  { title: "Applied ML topics", author: "Researcher" },
];

export default function CommunityPage() {
  return (
    <main style={{ maxWidth: 1200, margin: "0 auto", padding: "2rem" }}>
      <TopNav />
      <h1>Community</h1>
      <ul>
        {discussions.map((discussion) => (
          <li key={discussion.title} style={{ marginBottom: "1rem" }}>
            <strong>{discussion.title}</strong> <span>by {discussion.author}</span>
          </li>
        ))}
      </ul>
    </main>
  );
}
