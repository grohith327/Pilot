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
  creationDate: string
  lastModifiedDate: string
  impression: number
  successRate: number
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
          Last Updated Date: {props.lastModifiedDate}
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
            <Button variant="outline" size="sm" className="rounded-xl">
              {props.status === "Active" ? "Deactivate" : "Activate"}
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
