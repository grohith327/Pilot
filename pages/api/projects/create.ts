import { NextApiRequest, NextApiResponse } from "next";
import { ProjectStatus, supabase } from "@/lib/constants";

type ProjectCreateRequest = {
  name: string;
  description?: string;
  status?: string;
};

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { name, description, status } = req.body as ProjectCreateRequest;

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  if (!name) {
    return res.status(400).json({ error: "Name is a required field" });
  }

  const projectStatus = status || ProjectStatus.INACTIVE;

  const project = { name, description, status: projectStatus };
  const { data, error } = await supabase
    .from("projects")
    .insert(project)
    .select();

  if (error) {
    return res.status(500).json({ error: error.message });
  }

  return res.status(200).json(data[0]);
}
