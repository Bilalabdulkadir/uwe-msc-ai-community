import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "UWE MSc AI Community",
  description: "Community platform for MSc AI students, researchers, and alumni",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
