"use client"

import { formatDate } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

interface ElementCardProps {
  id: number
  name: string
  description: string
  status: string
  creation_time: string
  last_updated_time: string
  impression: number
  success_rate: number
  updateElementStatus: (elementId: string, status: string) => void
}

export function ElementCard(props: ElementCardProps) {
  return (
    <Card className="border-2 border-gray-200 rounded-xl">
      <CardHeader>
        <CardTitle>{props.name}</CardTitle>
        <CardDescription>{props.description}</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <p className="text-sm text-gray-500">
          Last Modified Date: {formatDate(props.last_updated_time)}
        </p>
        <div className="flex justify-between">
          <span
            className={
              props.status === "Active" ? "text-green-600" : "text-red-600"
            }
          >
            {props.status === "Active" ? "Active" : "Inactive"}
          </span>
          <div className="flex justify-end">
            <Button
              variant="outline"
              size="sm"
              className="rounded-xl"
              onClick={() =>
                props.updateElementStatus(
                  props.id.toString(),
                  props.status === "Active" ? "Inactive" : "Active"
                )
              }
            >
              {props.status === "Active" ? "Deactivate" : "Activate"}
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
