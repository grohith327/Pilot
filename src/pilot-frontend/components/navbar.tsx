import * as React from "react"
import Link from "next/link"

import { ThemeToggle } from "@/components/theme-toggle"
export function NavBar() {
  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background flex h-14 items-center gap-2 space-x-4 sm:justify-between sm:space-x-0 md:gap-6">
      <div className="flex flex-1 mx-2 gap-4 items-center">
        <div className="flex gap-6 md:gap-10">
          <Link href="/" className="flex items-center space-x-2">
            <span className="inline-block font-bold text-xl ml-2">🚀 Pilot</span>
          </Link>
        </div>
        <div className="flex-1 flex justify-end items-center space-x-4 mr-6">
          <nav className="flex items-center space-x-1">
            <ThemeToggle />
          </nav>
        </div>
      </div>
    </header>
  );
}