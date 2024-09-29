import { NextResponse } from 'next/server';
import axios from 'axios';

export async function POST(request: Request) {
  const body = await request.json();

  try {

    const response = await axios.post("http://localhost:63754/generate_story", body);
    return NextResponse.json(response.data);
  } catch (error) {
    console.error('Error generating story:', error);
    return NextResponse.json({ error: 'Error generating story' }, { status: 500 });
  }
}
