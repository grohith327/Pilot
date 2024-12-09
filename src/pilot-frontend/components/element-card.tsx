import { Badge } from "@/components/ui/badge"
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
        <Badge variant={props.status === "Active" ? "default" : "secondary"}>
          {props.status}
        </Badge>
      </CardContent>
    </Card>
  )
}
