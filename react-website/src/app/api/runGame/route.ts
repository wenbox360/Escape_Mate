import { NextResponse } from 'next/server';
import axios from 'axios';

export async function POST(request: Request) {
  const body = await request.json();

  try {
    const response = await axios.post("http://localhost:63754/run", body);
    return NextResponse.json(response.data);
  } catch (error) {
    console.error('Error running game', error);
    return NextResponse.json({ error: 'Error running game' }, { status: 500 });
  }
}