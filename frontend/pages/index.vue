<template>
  <div>
    <h1 class="mt-1">Approval Highlighter</h1>
    <b-form>
      <div class="cards mt-1">
        <div class="card">
          <span class="card__titile">あなたの意見</span>
          <b-form-textarea
            id="textarea"
            v-model="src"
            rows="10"
            placeholder="あなたの意見を入力してください．"
            :disabled="!showForm"
            no-resize
          ></b-form-textarea>
        </div>
        <div class="card">
          <span class="card__titile">比較したい意見</span>
          <b-form-textarea
            id="textarea"
            v-model="tgt"
            rows="10"
            placeholder="比較したい意見を入力してください．"
            :disabled="!showForm"
            no-resize
          ></b-form-textarea>
        </div>
      </div>
      <b-button class="mt-2" variant="info" @click="postForm" :disabled="!showForm">比較を開始する！</b-button>
    </b-form>
    <div v-if="!showForm">
      {{ analysisResult }}
      <b-button class="mt-2" variant="info" @click="showForm=true">戻る</b-button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { Component } from 'nuxt-property-decorator'

interface AnalysisResult {
  representative_sentence: string,
  tgt_sentences: string[],
  scores: number[]
}

@Component({})
export default class MainComponent extends Vue {
  showForm = true
  src: string = ''
  tgt: string = ''
  analysisResult: AnalysisResult = {
    representative_sentence: '',
    tgt_sentences: [],
    scores: []
  }

  async postForm () {
    this.showForm = false
    const params = {
      src: this.src,
      tgt: this.tgt
    }
    this.analysisResult = await this.$axios.$get('api/', {
      params: params,
      headers: {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    })
  }
}
</script>

<style>
body {
  text-align: center;
}

.h1 {
  font-size: 20px;
}

.card__titile {
  font-size: 1.3rem;
}

.card {
  display: inline-block;
  background-color: #b5d7da;
  padding: 10px;
  margin: 5px;
  height: 310px;
  width: 400px;
}
</style>
