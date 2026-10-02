import Link from 'next/link'

export default function Nav(){
  return (
    <nav>
      <ul>
        <li><Link href="/">Home</Link></li>
        <li><Link href="/dashboard">Dashboard</Link></li>
        <li><Link href="/community">Community</Link></li>
        <li><Link href="/discussions">Discussions</Link></li>
        <li><Link href="/events">Events</Link></li>
        <li><Link href="/projects">Projects</Link></li>
        <li><Link href="/resources">Resources</Link></li>
        <li><Link href="/mentorship">Mentorship</Link></li>
        <li><Link href="/publications">Publications</Link></li>
      </ul>
    </nav>
  )
}
