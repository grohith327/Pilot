"use client"

import { useState } from "react"

import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

interface CreateElementModalProps {
  isOpen: boolean
  onClose: (isOpen: boolean) => void
  onSave: (formData: {
    name: string
    description: string
    status: string
  }) => Promise<void>
}

export function CreateElementModal({
  isOpen,
  onClose,
  onSave,
}: CreateElementModalProps) {
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [status, setStatus] = useState("Inactive")

  const handleSubmit = () => {
    onSave({ name, description, status }).then(() => {
      setName("")
      setDescription("")
      setStatus("Inactive")
    })
  }

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogTrigger asChild>
        <Button variant="secondary" className="rounded-xl">
          Create Element
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Create new element</DialogTitle>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="name" className="text-right">
              Name <span className="text-red-500">*</span>
            </Label>
            <Input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="col-span-3"
              autoFocus
              required
            />
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="description" className="text-right">
              Description
            </Label>
            <Input
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="col-span-3"
            />
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="status" className="text-right">
              Status
            </Label>
            <Select value={status} onValueChange={setStatus}>
              <SelectTrigger className="col-span-3 rounded-xl">
                <SelectValue placeholder="Select a status" />
              </SelectTrigger>
              <SelectContent className="rounded-xl">
                <SelectItem value="Active" className="hover:bg-gray-100">
                  Active
                </SelectItem>
                <SelectItem value="Inactive" className="hover:bg-gray-100">
                  Inactive
                </SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>
        <DialogFooter>
          <Button type="submit" className="rounded-xl" onClick={handleSubmit}>
            Create Element
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
