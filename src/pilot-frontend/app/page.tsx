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
  const results = [
    {
      id: 1,
      name: "Project Alpha",
      description: "A revolutionary new software for project management",
      status: "Active",
      creationDate: "2023-06-15",
    },
    {
      id: 2,
      name: "Task Tracker Pro",
      description: "Advanced task tracking application for teams",
      status: "Inactive",
      creationDate: "2023-05-22",
    },
    {
      id: 3,
      name: "Data Analyzer X",
      description: "Powerful data analysis tool for businesses",
      status: "Inactive",
      creationDate: "2023-04-30",
    },
    {
      id: 4,
      name: "Cloud Storage Solution",
      description: "Secure and scalable cloud storage for enterprises",
      status: "Active",
      creationDate: "2023-06-01",
    },
    {
      id: 5,
      name: "AI Assistant",
      description: "Intelligent virtual assistant powered by machine learning",
      status: "Inactive",
      creationDate: "2023-06-10",
    },
  ]

  return (
    <div className="rounded-md w-full max-w-7xl">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead className="hidden md:table-cell">Description</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Date</TableHead>
            <TableHead className="text-right">Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {results.map((item) => (
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
              <TableCell className="text-right">
                <Button variant="outline" size="sm">View</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
