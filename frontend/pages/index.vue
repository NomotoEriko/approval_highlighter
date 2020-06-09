<template>
  <div>
    <h1 class="mt-1">Approval Highlighter</h1>
    <b-form>
      <div class="cards mt-1">
        <div class="card">
          <span class="card__title">あなたの意見</span>
          <b-form-textarea
            id="textarea"
            v-model="src"
            rows="10"
            placeholder="あなたの意見を入力してください．"
            :disabled="!showForm"
            required
            no-resize
          ></b-form-textarea>
        </div>
        <div class="card">
          <span class="card__title">比較したい意見</span>
          <b-form-textarea
            id="textarea"
            v-model="tgt"
            rows="10"
            placeholder="比較したい意見を入力してください．"
            :disabled="!showForm"
            required
            no-resize
          ></b-form-textarea>
        </div>
      </div>
      <b-button class="mt-2 mb-3" variant="info" @click="postForm" :disabled="!showForm">比較を開始する！</b-button>
    </b-form>
    <div v-if="!showForm">
      <div class="cards">
        <div class="card">
          <span class="card__title">中心文</span>
          <div class="card__content"><span>{{ analysisResult.representative_sentence }}</span></div>
        </div>
        <div class="card">
          <span class="card__title">ハイライト</span>
          <div class="card__content">
            <span v-for="(sentence, index) in analysisResult.tgt_sentences" :key="index" :style="'color:' + score2Color(analysisResult.scores[index])">
              {{ sentence }}
            </span>
          </div>
        </div>
      </div>
      <b-button class="mt-2" variant="info" @click="showForm=true">分析に戻る</b-button>
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

  score2Color (score: number): string {
    if (score > 0.9) { return '#1d6fc7' }  // 賛成
    if (score > 0.8) { return '#003671' }
    if (score < -0.8) { return '#632020' }
    if (score < -0.9) { return '#a70808' }  // 反対
    return '#000000'
  }

  async postForm () {
    if (this.src.length == 0 || this.tgt.length == 0) {return}
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
  font-size: 18px;
}

.card__title {
  font-size: 1.3rem;
}

.card__content {
  display: inline-grid;
  font-size: 1rem;
  text-align: left;
  overflow: scroll;
  height: 250px;
  width: 375px;
  background-color: #ffffff
}

.card__content span {
  margin: 2px;
}

.card {
  display: inline-block;
  background-color: #b5d7da;
  padding: 10px;
  padding-top: 2px;
  margin: 5px;
  height: 300px;
  width: 400px;
}
</style>
