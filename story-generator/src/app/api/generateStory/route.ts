import { NextResponse } from 'next/server';
import { b } from '../../../../baml_client';
import type { StoryParams } from '../../../../baml_client';

export async function POST(request: Request) {
  const { theme, difficulty, stage_physical_descriptions, num_players, time_limit_min } = await request.json();

  try {
    const storyParams: StoryParams = {
      theme,
      difficulty,
      stage_physical_descriptions,
      num_players,
      time_limit_min,
    };

    const output = await b.GenerateStory(storyParams);

    return NextResponse.json(output);
  } catch (error) {
    console.error('Error generating story:', error);
    return NextResponse.json({ error: 'Error generating story' }, { status: 500 });
  }
}
