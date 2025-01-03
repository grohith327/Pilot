"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"

import { API_URL, formatDate } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

export default function Home() {
  const router = useRouter()
  const [results, setResults] = useState<any[]>([])

  useEffect(() => {
    fetch(`${API_URL}/projects/browse`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
      })
      .then((data) => setResults(data.projects))
  }, [])

  const onProjectClick = (id: number) => {
    router.push(`/projects/${id}`)
  }

  return (
    <div className="flex items-center justify-center w-screen mt-8">
      <main className="min-h-screen bg-background">
        {/* 
        TODO: Add filtering logic and uncomment the code below
        <ProjectSearchFilter /> 
        */}
        <div className="p-4">
          {/* 
          TODO: Add searching logic and uncomment the code below
          <div className="flex justify-center">
            <SearchBar />
            <Button className="ml-4 rounded-xl" size="md" variant="outline">
              Search
            </Button>
          </div> 
          */}
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Name</TableHead>
                <TableHead className="hidden md:table-cell">
                  Description
                </TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Creation Date</TableHead>
                <TableHead>Last Modified Date</TableHead>
                <TableHead className="text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {results.map((item: any) => (
                <TableRow key={item.id}>
                  <TableCell className="font-medium">{item.name}</TableCell>
                  <TableCell className="hidden md:table-cell">
                    {item.description}
                  </TableCell>
                  <TableCell>
                    <Badge
                      variant={
                        item.status === "Active" ? "default" : "secondary"
                      }
                      className={
                        item.status === "Active"
                          ? "bg-green-500 hover:bg-green-600"
                          : ""
                      }
                    >
                      {item.status}
                    </Badge>
                  </TableCell>
                  <TableCell>{formatDate(item.creation_time)}</TableCell>
                  <TableCell>{formatDate(item.last_updated_time)}</TableCell>
                  <TableCell className="text-right">
                    <Button
                      variant="secondary"
                      size="default"
                      className="rounded-xl"
                      onClick={() => onProjectClick(item.id)}
                    >
                      View
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </main>
    </div>
  )
}
