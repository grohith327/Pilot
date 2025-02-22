import { NextApiRequest, NextApiResponse } from "next";
import { supabase } from "@/lib/constants";

type Project = {
  id: string,
  name: string,
  description: string,
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id } = req.query;

  try {
    if (req.method == "GET") {
      const project = await getProject(id as string);
      return res.status(200).json(project);
    }
  } catch (error) {
    return res.status(500).json({ error: (error as Error).message });
  }

  return res.status(405).json({ error: "Method not allowed" });
}


async function getProject(id: string) {
  const { data, error } = await supabase
    .from("projects")
    .select("*")
    .eq("id", id);

  if (error) {
    throw new Error(error.message);
  }

  return data;
}
