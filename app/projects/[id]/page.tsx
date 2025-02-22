"use client"

import { useEffect, useState } from "react"
import { useParams } from "next/navigation"

import { API_URL, formatDate } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { CreateElementModal } from "@/components/create-element-modal"
import { ElementCard } from "@/components/element-card"
import { Loader } from "@/components/loader"

export default function ProjectPage() {
  const [projectData, setProjectData] = useState<any>()
  const [isCreateElementModalOpen, setIsCreateElementModalOpen] =
    useState(false)
  const id = "13234"

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

  const handleSave = async (formData: {
    name: string
    description: string
    status: string
  }) => {
    if (formData.name === "") {
      // Add alert to show name is required
      return
    }

    const elementData = {
      ...formData,
      project_id: id,
    }

    fetch(`${API_URL}/elements/create`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(elementData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
      })
      .then((data) => {
        setIsCreateElementModalOpen(false)
        setProjectData({
          ...projectData,
          elements: [...projectData.elements, data.data],
        })
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
          <div className="flex items-center space-x-2">
            <CreateElementModal
              isOpen={isCreateElementModalOpen}
              onClose={setIsCreateElementModalOpen}
              onSave={handleSave}
            />
            <Button
              variant="outline"
              className="rounded-xl"
              onClick={() =>
                updateProjectStatus(
                  projectData.status === "Active" ? "Inactive" : "Active"
                )
              }
            >
              {projectData.status === "Active"
                ? "Deactivate Project"
                : "Activate Project"}
            </Button>
          </div>
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
