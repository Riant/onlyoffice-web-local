<template lang="pug">
.loading-progress(v-if="visible")
  .loading-mask
  .loading-content
    .loading-spinner
    .loading-text {{ text }}
    .progress-bar(v-if="showProgress")
      .progress-fill(:style="{ width: progress + '%' }")
    .progress-percent(v-if="showProgress") {{ progress }}%
</template>

<script lang="ts">
export default {
  name: 'LoadingProgress',
  props: {
    visible: { type: Boolean, default: false },
    text: { type: String, default: '加载中...' },
    progress: { type: Number, default: 0 },
    showProgress: { type: Boolean, default: false }
  }
}
</script>

<style lang="scss" scoped>
.loading-progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-mask {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
}

.loading-content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 60px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.loading-spinner {
  width: 32px;
  height: 32px;
  margin-bottom: 20px;
  border: 3px solid #e4e7ed;
  border-top-color: #409eff;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.loading-text {
  font-size: 16px;
  color: #333;
  margin-bottom: 16px;
}

.progress-bar {
  width: 200px;
  height: 6px;
  background: #e4e7ed;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 10px;

  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #409eff, #67c23a);
    border-radius: 3px;
    transition: width 0.3s ease;
  }
}

.progress-percent {
  font-size: 14px;
  color: #909399;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
