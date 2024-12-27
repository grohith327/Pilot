import React from "react"
import { Loader2 } from "lucide-react"

import { cn } from "@/lib/utils"

export const Loader = () => {
  return (
    <Loader2 className={cn("my-28 h-12 w-12 text-primary/60 animate-spin")} />
  )
}