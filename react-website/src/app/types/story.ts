// types/story.ts

export interface StoryParams {
  theme: string;
  stage_physical_descriptions: string[];
  num_players: number;
  time_limit_min: number;
  difficulty: string;
}

export interface Stage {
  description: string;
  success_message: string;
  failure_message: string;
}
  
export interface Story {
  intro: string;
  stages: Stage[];
  good_ending: string;
  bad_ending: string;
}
  