"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { PlusCircle, X } from "lucide-react"

import { API_URL } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"

interface AddElement {
  name: string
  description: string
  status: string
}

export default function CreateProjectPage() {
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [status, setStatus] = useState("active")
  const [elements, setElements] = useState<AddElement[]>([])

  const router = useRouter()

  const addElement = () => {
    setElements([...elements, { name: "", description: "", status: "" }])
  }

  const removeElement = (index: number) => {
    setElements(elements.filter((_, idx) => idx !== index))
  }

  const updateElement = (index: number, fieldName: string, value: string) => {
    setElements(
      elements.map((element, idx) =>
        idx === index ? { ...element, [fieldName]: value } : element
      )
    )
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log(JSON.stringify({ name, description, status, elements }))
    fetch(`${API_URL}/projects/create`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, description, status, elements }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        return response.json()
      })
      .then((data) => {
        router.push(`/projects/${data.id}`)
      })
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6 mx-auto w-1/4 mt-8 p-6">
      <div className="space-y-2">
        <Label htmlFor="name">
          Name <span className="text-red-500">*</span>
        </Label>
        <Input
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="description">Description</Label>
        <Textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows={3}
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="status">Status</Label>
        <Select value={status} onValueChange={setStatus}>
          <SelectTrigger id="status" className="rounded-xl">
            <SelectValue placeholder="Select status" />
          </SelectTrigger>
          <SelectContent className="rounded-xl">
            <SelectItem value="Active">Active</SelectItem>
            <SelectItem value="Inactive">Inactive</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="space-y-4">
        <Label>Elements</Label>
        {elements.map((element, index) => (
          <div
            key={index}
            className="flex items-center flex-col space-y-2 border-2 border-gray-200 rounded-xl p-4"
          >
            <Input
              value={element.name}
              onChange={(e) => updateElement(index, "name", e.target.value)}
              placeholder="Element name"
              aria-label="Element name"
            />
            <Input
              value={element.description}
              onChange={(e) =>
                updateElement(index, "description", e.target.value)
              }
              placeholder="Element description"
              aria-label="Element description"
            />
            <Select
              value={element.status}
              onValueChange={(e) => updateElement(index, "status", e)}
            >
              <SelectTrigger id="status" className="rounded-xl">
                <SelectValue placeholder="Select status" />
              </SelectTrigger>
              <SelectContent className="rounded-xl">
                <SelectItem value="Active">Active</SelectItem>
                <SelectItem value="Inactive">Inactive</SelectItem>
              </SelectContent>
            </Select>
            <Button
              type="button"
              variant="outline"
              onClick={() => removeElement(index)}
              aria-label="Remove element"
              className="w-full rounded-xl"
            >
              Remove Element <X className="h-4 w-4" />
            </Button>
          </div>
        ))}
        <Button
          type="button"
          variant="secondary"
          onClick={addElement}
          className="w-full rounded-xl"
        >
          <PlusCircle className="mr-2 h-4 w-4" /> Add Element
        </Button>
      </div>

      <Button type="submit" className="w-full rounded-xl">
        Submit
      </Button>
    </form>
  )
}
