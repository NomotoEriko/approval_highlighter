<template>
  <div>
    <h1 class="mt-1">Approval Highlighter</h1>
    <div class="cards mt-1">
      <div class="card">
        <span class="card__titile">あなたの意見</span>
        <b-form-textarea
          id="textarea"
          v-model="src"
          rows="10"
          placeholder="あなたの意見を入力してください．"
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
          no-resize
        ></b-form-textarea>
      </div>
    </div>
    <b-button class="mt-2" variant="info">比較を開始する！</b-button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { Component } from 'nuxt-property-decorator'
import axios from 'axios'

@Component({})
export default class MainComponent extends Vue {
  src: string = ''
  tgt: string = ''

  async asyncData () {
    const { data } = await axios.get('http://backend:3000/')
    return { data }
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
