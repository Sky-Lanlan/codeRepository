Page({

  /**
   * 页面的初始数据
   */
  data: {
    result: 0,
    output: '',

    m1: false, m2: false, m3: false, m4: false, m5: false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {


  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    this.setData({
      m1: getApp().globalData.m1,
      m2: getApp().globalData.m2,
      m3: getApp().globalData.m3,
      m4: getApp().globalData.m4,
      m5: getApp().globalData.m5,
    })

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  check_matrix: function (res) {

    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'
    console.log("变量的id：" + res.currentTarget.id);
    // console.log(res);
    var ids = res.currentTarget.id;
    wx.navigateTo({
      url: '/pages/matrix-input/matrix-input?id=' + ids,
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    });
  },

  help: function () {
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'
    wx.navigateTo({
      url: '/pages/help/help?id=' + 0,
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    })
  },

  calc: function (res) {
    var that = this;
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'
    wx.request({
      url: 'https://lanlan.mynatapp.cc',
      data: {
        'm1': getApp().globalData.matrix[0].content.replace(/%/g, ''),
        'm2': getApp().globalData.matrix[1].content.replace(/%/g, ''),
        'm3': getApp().globalData.matrix[2].content.replace(/%/g, ''),
        'm4': getApp().globalData.matrix[3].content.replace(/%/g, ''),
        'm5': getApp().globalData.matrix[4].content.replace(/%/g, ''),
        'command': res.detail.value.command
      },
      dataType: 'json',
      responseType: 'text',
      success: function (res) {
        console.log(res.data);
        that.setData({
          output: res.data,
          
        })
      },
      fail: function (res) {
        console.log("发送失败");
        
      },
      complete: function (res) {
        console.log("发送结束")
       
        if (that.data.output.indexOf("not found")!=-1){
          that.setData({
            output: {data:"服务端未开启，请联系作者，qq:2235826534"},
          })
        }
      },
    })

  },
  scroll: function (res) {

  },
  upper: function () {

  },
  lower: function () {

  }
})