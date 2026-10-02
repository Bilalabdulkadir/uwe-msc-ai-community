import Link from "next/link";

const navItems = [
  ["/", "Home"],
  ["/dashboard", "Dashboard"],
  ["/community", "Community"],
  ["/events", "Events"],
  ["/projects", "Projects"],
  ["/resources", "Resources"],
  ["/discussions", "Discussions"],
  ["/mentorship", "Mentorship"],
  ["/publications", "Publications"],
];

export default function TopNav() {
  return (
    <nav style={{ padding: "1rem 1.5rem", borderBottom: "1px solid #ddd", display: "flex", gap: "1rem", flexWrap: "wrap" }}>
      {navItems.map(([href, label]) => (
        <Link key={href} href={href} style={{ textDecoration: "none", color: "#0f172a" }}>
          {label}
        </Link>
      ))}
    </nav>
  );
}
