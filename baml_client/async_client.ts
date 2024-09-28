/*************************************************************************************************

Welcome to Baml! To use this generated code, please run one of the following:

$ npm install @boundaryml/baml
$ yarn add @boundaryml/baml
$ pnpm add @boundaryml/baml

*************************************************************************************************/

// This file was generated by BAML: do not edit it. Instead, edit the BAML
// files and re-generate this code.
//
/* eslint-disable */
// tslint:disable
// @ts-nocheck
// biome-ignore format: autogenerated code
import { BamlRuntime, FunctionResult, BamlCtxManager, BamlStream, Image, ClientRegistry } from "@boundaryml/baml"
import {Story, StoryParams} from "./types"
import TypeBuilder from "./type_builder"
import { DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME } from "./globals"

export type RecursivePartialNull<T> = T extends object
  ? {
      [P in keyof T]?: RecursivePartialNull<T[P]>;
    }
  : T | null;

export class BamlAsyncClient {
  private runtime: BamlRuntime
  private ctx_manager: BamlCtxManager
  private stream_client: BamlStreamClient

  constructor(runtime: BamlRuntime, ctx_manager: BamlCtxManager) {
    this.runtime = runtime
    this.ctx_manager = ctx_manager
    this.stream_client = new BamlStreamClient(runtime, ctx_manager)
  }

  get stream() {
    return this.stream_client
  }  

  
  async GenerateStory(
      params: StoryParams,
      __baml_options__?: { tb?: TypeBuilder, clientRegistry?: ClientRegistry }
  ): Promise<Story> {
    const raw = await this.runtime.callFunction(
      "GenerateStory",
      {
        "params": params
      },
      this.ctx_manager.cloneContext(),
      __baml_options__?.tb?.__tb(),
      __baml_options__?.clientRegistry,
    )
    return raw.parsed() as Story
  }
  
}

class BamlStreamClient {
  constructor(private runtime: BamlRuntime, private ctx_manager: BamlCtxManager) {}

  
  GenerateStory(
      params: StoryParams,
      __baml_options__?: { tb?: TypeBuilder, clientRegistry?: ClientRegistry }
  ): BamlStream<RecursivePartialNull<Story>, Story> {
    const raw = this.runtime.streamFunction(
      "GenerateStory",
      {
        "params": params
      },
      undefined,
      this.ctx_manager.cloneContext(),
      __baml_options__?.tb?.__tb(),
      __baml_options__?.clientRegistry,
    )
    return new BamlStream<RecursivePartialNull<Story>, Story>(
      raw,
      (a): a is RecursivePartialNull<Story> => a,
      (a): a is Story => a,
      this.ctx_manager.cloneContext(),
      __baml_options__?.tb?.__tb(),
    )
  }
  
}

export const b = new BamlAsyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)