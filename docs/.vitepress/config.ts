import { defineConfig } from 'vitepress'

const config = defineConfig({
  base: '/Stock-Learning-Skill/',
  lang: 'zh-CN',
  title: 'A股学习站',
  description: '为零基础投资者打造的A股入门教程与每日市场分析',
  cleanUrls: true,
  ignoreDeadLinks: true,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['meta', { name: 'theme-color', content: '#1a73e8' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:locale', content: 'zh-CN' }],
    ['meta', { name: 'og:site_name', content: 'A股学习站' }],
  ],
  markdown: {
    lineNumbers: true,
    container: {
      tipLabel: '💡 提示',
      warningLabel: '⚠️ 注意',
      dangerLabel: '🚨 风险',
      infoLabel: '📋 信息',
      detailsLabel: '详情',
    },
  },
  themeConfig: {
    logo: { src: '/logo.png', width: 24, height: 24 },
    lastUpdated: { text: '最近更新', formatOptions: { dateStyle: 'short', timeStyle: 'medium' } },
    darkModeSwitchLabel: '深色模式',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部',
    outline: { level: 'deep', label: '当前页' },
    siteTitle: '📈 A股学习站',
    docFooter: { prev: '上一篇', next: '下一篇' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/raopan2021/Stock-Learning-Skill' },
    ],
    nav: [
      { text: '📚 入门教程', link: '/guide/' },
      { text: '📰 每日日报', link: '/daily/' },
    ],
    sidebar: {
      '/guide/': [
        {
          text: '入门基础',
          items: [
            { text: '前言', link: '/guide/' },
            { text: '第一课：股票是什么', link: '/guide/01-what-is-stock' },
            { text: '第二课：如何迈出第一步', link: '/guide/02-how-to-start' },
            { text: '第三课：A股交易规则', link: '/guide/03-trading-rules' },
          ],
        },
        {
          text: '看懂市场',
          items: [
            { text: '第四课：什么是指数', link: '/guide/04-what-is-index' },
            { text: '第五课：板块与行业', link: '/guide/05-industry' },
            { text: '第六课：盘面基础知识', link: '/guide/06-chart-basics' },
          ],
        },
        {
          text: '基本面分析',
          items: [
            { text: '第七课：读懂财报三张表', link: '/guide/07-financial-statements' },
            { text: '第八课：常用估值指标', link: '/guide/08-valuation-metrics' },
          ],
        },
        {
          text: '技术分析入门',
          items: [
            { text: '第九课：K线基础', link: '/guide/09-kline-basics' },
            { text: '第十课：均线系统', link: '/guide/10-moving-average' },
            { text: '第十一课：MACD指标', link: '/guide/11-macd' },
          ],
        },
        {
          text: '投资理念',
          items: [
            { text: '第十二课：价值投资', link: '/guide/12-value-investing' },
            { text: '第十三课：行业轮动', link: '/guide/13-sector-rotation' },
          ],
        },
        {
          text: '基金入门',
          items: [
            { text: '第十四课：ETF基金', link: '/guide/14-etf' },
            { text: '第十五课：基金定投', link: '/guide/15定投' },
          ],
        },
        {
          text: '风险控制',
          items: [
            { text: '第十六课：仓位管理', link: '/guide/16-position-management' },
            { text: '第十七课：止损与止盈', link: '/guide/17-stop-loss' },
          ],
        },
        {
          text: '实战技巧',
          items: [
            { text: '第十八课：选股思路', link: '/guide/18-stock-picking' },
            { text: '第十九课：读盘技巧', link: '/guide/19-reading-charts' },
            { text: '第二十课：下单与成交', link: '/guide/20-order-execution' },
          ],
        },
      ],
      '/daily/': [
        {
          text: '2026年',
          items: [
            { text: '日报索引', link: '/daily/' },
            { text: '2026-04', link: '/daily/2026-04' },
          ],
        },
      ],
    },
  },
})

export default config
