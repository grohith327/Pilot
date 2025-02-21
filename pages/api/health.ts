import type { NextApiRequest, NextApiResponse } from "next";

type HealthResponse = {
    message: string
};

export default function handler(req: NextApiRequest, res: NextApiResponse<HealthResponse>) {
    res.status(200).json({message: "healthy"});
}