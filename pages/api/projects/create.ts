import { NextApiRequest, NextApiResponse } from "next";
import { supabase } from "@/lib/constants";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { name, description } = req.body;

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  // Sanitize input before storing in database
  const { data, error } = await supabase
    .from("projects")
    .insert({ name, description });

  if (error) {
    return res.status(500).json({ error: error.message });
  }

  return res.status(200).json(data);
}
