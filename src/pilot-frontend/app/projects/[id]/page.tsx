import { ChevronDownIcon } from "lucide-react"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Separator } from "@/components/ui/separator"
import { ElementCard } from "@/components/element-card"

export default function ProjectPage() {
  const dummyProjectData = {
    id: 1,
    name: "Project 1",
    description: "This is a project",
    status: "Active",
    creationDate: "2024-01-01",
    lastModifiedDate: "2024-01-01",
    elements: [
      {
        id: 1,
        name: "Element 1",
        description: "This is an element 1",
        status: "Active",
        creationDate: "2024-01-01",
        lastModifiedDate: "2024-01-01",
        impression: 100,
        successRate: 0.75,
      },
      {
        id: 2,
        name: "Element 2",
        description: "This is an element 2",
        status: "Active",
        creationDate: "2024-01-01",
        lastModifiedDate: "2024-01-01",
        impression: 90,
        successRate: 0.65,
      },
      {
        id: 3,
        name: "Element 3",
        description: "This is an element 3",
        status: "Inactive",
        creationDate: "2024-01-01",
        lastModifiedDate: "2024-01-01",
        impression: 80,
        successRate: 0.55,
      },
    ],
  }

  return (
    <div className="container mx-auto max-w-7xl px-4 py-8 md:px-6">
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-2xl font-bold">{dummyProjectData.name}</h1>
          <div className="flex items-center space-x-2">
            <p className="text-gray-500 text-sm mt-4">
              {dummyProjectData.description}
            </p>
            <Badge
              variant={
                dummyProjectData.status === "Active" ? "default" : "secondary"
              }
              className="mt-4"
            >
              {dummyProjectData.status}
            </Badge>
          </div>
        </div>

        <div className="text-right space-y-4">
          <p className="text-sm text-gray-500 mt-2">
            Last Modified Date: {dummyProjectData.lastModifiedDate}
          </p>
          <DropdownMenu>
            <DropdownMenuTrigger>
              <Button className="rounded-xl" size="smd" variant="secondary">
                Actions <ChevronDownIcon className="w-4 h-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem>Add Element</DropdownMenuItem>
              <DropdownMenuItem>Deactivate Project</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>

      <Separator className="my-4" />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {dummyProjectData.elements.map((element) => (
          <ElementCard key={element.id} {...element} />
        ))}
      </div>
    </div>
  )
}
