import { NextApiRequest, NextApiResponse } from "next";

type Project = {
  id: string,
  name: string,
  description: string,
}

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id }  = req.query;

  if (req.method == "GET") {
    let project: Project = {
      id: "1234",
      name: "Test",
      description: "desc"
    };
    return res.status(200).json(project);
  }

  return res.status(405).json({error: "Method not allowed"});
}