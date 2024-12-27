"use client"

import { useEffect, useState } from "react"
import { useParams } from "next/navigation"
import { ChevronDownIcon } from "lucide-react"

import { API_URL, formatDate } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Separator } from "@/components/ui/separator"
import { ElementCard } from "@/components/element-card"
import { Loader } from "@/components/loader"

export default function ProjectPage() {
  const [projectData, setProjectData] = useState<any>()
  const { id } = useParams()

  useEffect(() => {
    fetch(`${API_URL}/projects/${id}`)
      .then((response) => response.json())
      .then((data) => setProjectData(data))
  }, [])

  const updateProjectStatus = (status: string) => {
    fetch(`${API_URL}/projects/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ status: status }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
      })
      .then((data) => {
        setProjectData({ ...projectData, status: status })
      })
  }

  const updateElementStatus = (elementId: string, status: string) => {
    fetch(`${API_URL}/elements/${elementId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ status: status }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
      })
      .then((data) => {
        setProjectData({
          ...projectData,
          elements: projectData.elements.map((element: any) =>
            element.id === elementId ? { ...element, status: status } : element
          ),
        })
      })
  }

  return projectData ? (
    <div className="container mx-auto max-w-7xl px-4 py-8 md:px-6">
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-2xl font-bold">{projectData.name}</h1>
          <div className="flex items-center space-x-2">
            <p className="text-gray-500 text-sm mt-4">
              {projectData.description}
            </p>
            <span
              className={
                projectData.status === "Active"
                  ? "text-green-600 mt-4"
                  : "text-red-600 mt-4"
              }
            >
              {projectData.status === "Active" ? "Active" : "Inactive"}
            </span>
          </div>
        </div>

        <div className="text-right space-y-4">
          <p className="text-sm text-gray-500 mt-2">
            Last Modified Date: {formatDate(projectData.last_updated_time)}
          </p>
          <DropdownMenu>
            <DropdownMenuTrigger>
              <Button className="rounded-xl" size="smd" variant="secondary">
                Actions <ChevronDownIcon className="w-4 h-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem>Add Element</DropdownMenuItem>
              <DropdownMenuItem
                onClick={() =>
                  updateProjectStatus(
                    projectData.status === "Active" ? "Inactive" : "Active"
                  )
                }
              >
                {projectData.status === "Active"
                  ? "Deactivate Project"
                  : "Activate Project"}
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>

      <Separator className="my-4" />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {projectData.elements.map((element: any) => (
          <ElementCard
            key={element.id}
            updateElementStatus={updateElementStatus}
            {...element}
          />
        ))}
      </div>
    </div>
  ) : (
    <div className="flex justify-center items-center h-screen">
      <Loader />
    </div>
  )
}
