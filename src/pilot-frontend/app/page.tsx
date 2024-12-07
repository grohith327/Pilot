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
import { SearchBar } from "@/components/search-bar"
import ProjectSearchFilter from "@/components/project-search-filter"

export default function Home() {
  const results = [
    {
      id: 1,
      name: "Project Alpha",
      description: "A revolutionary new software for project management",
      status: "Active",
      creationDate: "2023-06-15",
      lastModifiedDate: "2023-06-15"
    },
    {
      id: 2,
      name: "Task Tracker Pro",
      description: "Advanced task tracking application for teams",
      status: "Inactive",
      creationDate: "2023-05-22",
      lastModifiedDate: "2023-06-15"
    },
    {
      id: 3,
      name: "Data Analyzer X",
      description: "Powerful data analysis tool for businesses",
      status: "Inactive",
      creationDate: "2023-04-30",
      lastModifiedDate: "2023-06-15"
    },
    {
      id: 4,
      name: "Cloud Storage Solution",
      description: "Secure and scalable cloud storage for enterprises",
      status: "Active",
      creationDate: "2023-06-01",
      lastModifiedDate: "2023-06-15"
    },
    {
      id: 5,
      name: "AI Assistant",
      description: "Intelligent virtual assistant powered by machine learning",
      status: "Inactive",
      creationDate: "2023-06-10",
      lastModifiedDate: "2023-06-15"
    },
  ]

  // Duplicate the items in results to have more data for testing
  const resultsWithDuplicates = [...results, ...results, ...results, ...results, ...results]

  return (
    <main className="min-h-screen bg-background">
      <ProjectSearchFilter />
      <div className="p-4 ml-64">
        <div className="flex justify-center">
          <SearchBar />
          <Button className="ml-4 rounded-xl" size="md" variant="outline">Search</Button>
        </div>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Name</TableHead>
              <TableHead className="hidden md:table-cell">Description</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Creation Date</TableHead>
              <TableHead>Last Modified Date</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {resultsWithDuplicates.map((item) => (
              <TableRow key={item.id}>
                <TableCell className="font-medium">{item.name}</TableCell>
                <TableCell className="hidden md:table-cell">{item.description}</TableCell>
                <TableCell>
                  <Badge
                    variant={item.status === 'Active' ? 'default' : 'secondary'}
                  >
                    {item.status}
                  </Badge>
                </TableCell>
                <TableCell>{item.creationDate}</TableCell>
                <TableCell>{item.lastModifiedDate}</TableCell>
                <TableCell className="text-right">
                  <Button variant="secondary" size="default" className="rounded-xl">View</Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </main>
  );
}
