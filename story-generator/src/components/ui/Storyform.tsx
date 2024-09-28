"use client";

import React, { useState } from 'react';
import axios from 'axios';
import { StoryParams, Story } from '../../app/types/story';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

const StoryForm: React.FC = () => {
  const [theme, setTheme] = useState<string>('');
  const [difficulty, setDifficulty] = useState<string>('Easy');
  const [stages, setStages] = useState<string[]>(['']);
  const [numPlayers, setNumPlayers] = useState<number>(2);
  const [timeLimit, setTimeLimit] = useState<number>(20);
  const [story, setStory] = useState<Story | null>(null);

  const handleAddStage = () => setStages([...stages, '']);
  const handleStageChange = (index: number, value: string) => {
    const newStages = [...stages];
    newStages[index] = value;
    setStages(newStages);
  };

  const generateStory = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post<Story>('/api/generateStory', {
        theme,
        difficulty,
        stage_physical_descriptions: stages,
        num_players: numPlayers,
        time_limit_min: timeLimit,
      });
      setStory(response.data);
    } catch (error) {
      console.error('Error generating story:', error);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-background text-foreground p-4">
      <div className="story-form bg-foreground text-background rounded-lg shadow-lg p-6 w-full max-w-md bg-zinc-800">
        <form onSubmit={generateStory} className="flex flex-col space-y-4">
          <h1 className="text-3xl font-bold mb-6 text-white text-center">Generate Your Escape Room Story</h1>

          {/* Theme Input */}
          <Input 
            className="w-full bg-white text-black"
            placeholder="Enter Theme"
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
          />

          {/* Difficulty Select */}
          <Select onValueChange={(value) => setDifficulty(value)} defaultValue={difficulty}>
            <SelectTrigger className="w-full bg-white text-black">
              <SelectValue placeholder="Select Difficulty" />
            </SelectTrigger>
            <SelectContent className="bg-white text-black">
              <SelectItem value="Easy">Easy</SelectItem>
              <SelectItem value="Medium">Medium</SelectItem>
              <SelectItem value="Hard">Hard</SelectItem>
            </SelectContent>
          </Select>

          {/* Stages Input */}
          {stages.map((stage, index) => (
            <Input
              key={index}
              className="w-full bg-white text-black"
              placeholder={`Stage ${index + 1} Description`}
              value={stage}
              onChange={(e) => handleStageChange(index, e.target.value)}
            />
          ))}
          <Button variant="outline" onClick={handleAddStage} className="self-center">
            Add Stage
          </Button>

          {/* Number of Players & Time Limit */}
          <Input
            className="w-full bg-white text-black"
            type="number"
            placeholder="Number of Players"
            value={numPlayers}
            onChange={(e) => setNumPlayers(parseInt(e.target.value))}
          />
          <Input
            className="w-full bg-white text-black"
            type="number"
            placeholder="Time Limit (in minutes)"
            value={timeLimit}
            onChange={(e) => setTimeLimit(parseInt(e.target.value))}
          />

          {/* Submit Button */}
          <Button type="submit" variant="default" className="w-full">
            Generate Story
          </Button>
        </form>

        {/* Display Generated Story */}
        {story && (
          <div className="mt-8 p-4 bg-background text-foreground rounded-md shadow-md">
            <h2 className="text-xl font-bold">Generated Story</h2>
            <p><strong>Intro:</strong> {story.intro}</p>
            <h3 className="font-bold">Stages:</h3>
            <ul>
              {story.stage_descriptions.map((stage, index) => (
                <li key={index}>Stage {index + 1}: {stage}</li>
              ))}
            </ul>
            <p><strong>Good Ending:</strong> {story.good_ending}</p>
            <p><strong>Bad Ending:</strong> {story.bad_ending}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default StoryForm;
