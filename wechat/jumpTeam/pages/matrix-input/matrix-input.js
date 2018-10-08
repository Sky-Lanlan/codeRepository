Page({

  /**
   * 页面的初始数据
   * count 每一行有多少个字符
   * content 记录最后发送数据
   * line 记录当前行号
   * lcontent  记录每一行数据
   */
  data: {

    clt_it: '<--',
    id: 0,
    count: 0,
    line: 0,
    lcontent: [{ num: '', pointer: false }, { num: '', pointer: false }, { num: '', pointer: false },
    { num: '', pointer: false }, { num: '', pointer: false }, { num: '', pointer: false }, { num: '', pointer: false },
    { num: '', pointer: false }, { num: '', pointer: false }, { num: '', pointer: false }, { num: '', pointer: false }

    ],

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {



    var temp = new String((getApp().globalData.matrix[options.id]).content);
    var temp2 = new Array();
    if (temp != '') {
      temp2 = temp.split('%');

    } else {
      temp2 = '';
    }

    var oldData = [];//准备数据
    var i, length = 0, j;


    for (i = 0, j = 0; i < temp2.length - 1; i++) {
      oldData[i] = new Object();

      oldData[i].num = temp2[i + 1];

    }

    if (temp2 != '') {
      length = temp2[i - 1].length;
    }

    for (; i < 10; i++) {
      oldData[i] = new Object();
      oldData[i].num = '';
    }

    var thisline = 0;
    console.log('temp:' + temp);
    if (temp.indexOf("%") != -1) {
      thisline = temp.split("%").length - 3;
    }
    console.log('当前行数' + thisline);
    var counter;
    if (temp != '') {

      counter = temp.split("%")[thisline + 1].length;
    } else {
      counter = 0;
    }
    console.log("当前行字数" + counter);
    var tPointer = 'lcontent[' + thisline + '].pointer';
    this.setData({
      count: counter,
      id: options.id,
      line: thisline,
      lcontent: oldData,
      [tPointer]: true,
    });
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
  clicked: function (res) {

    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'

    var currentLine = this.data.line;//获取当前行数
    var temp = 'lcontent[' + currentLine + '].num';
    this.setData({

      [temp]: this.data.lcontent[currentLine].num + res.currentTarget.id,
      count: this.data.count + 1,
    })
  },

  back: function () {
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/back.wav'

    var currentLine = this.data.line;//获取当前行数
    // console.log("当前行"+currentLine);
    // console.log("当前行字数"+this.data.count);
    //如果当前行为空

    if (this.data.count == 0) {
      var ccurent;
      var counter;
      //如果当前行为第一行
      if (currentLine == 0) {
        ccurent = 0;
      } else {

        ccurent = currentLine - 1;
        counter = 0;
        console.log("当前行" + ccurent);
        var tPointer2 = 'lcontent[' + currentLine + '].pointer';
        this.setData({
          [tPointer2]: false,
        })
      }

      var tPointer = 'lcontent[' + ccurent + '].pointer';
      this.setData({
        line: ccurent,
        count: this.data.lcontent[ccurent].num.length,
        [tPointer]: true,
      })
      return;
    }

    var temp = 'lcontent[' + currentLine + '].num';
    //碰及首
    if (currentLine == 0 && this.data.count == 0) {
      return;
    }
    this.setData({
      [temp]: this.data.lcontent[currentLine].num.substring(0, this.data.lcontent[currentLine].num.length - 1),
      count: this.data.count - 1,
    })
    console.log("当前行" + currentLine);
    console.log("当前行字数" + this.data.count);
  },
  end: function (res) {
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'


    var result = '';
    for (var i = 0; i <= this.data.line; i++) {
      result = result + this.data.lcontent[i].num + '%';
    }
    console.log("result:" + result);
    var falg = true;
    if (result == "%") { falg = false }
    if (this.data.id == 0) {
      console.log("in");
      getApp().globalData.m1 = falg;
    } else if (this.data.id == 1) {
      getApp().globalData.m2 = falg;
    } else if (this.data.id == 2) {
      getApp().globalData.m3 = falg;
    } else if (this.data.id == 3) {
      getApp().globalData.m4 = falg;
    } else {
      getApp().globalData.m5 = falg;
    }
    console.log("全局变量" + getApp().globalData.m2)

    getApp().globalData.matrix[this.data.id].content = "%" + result;
    wx.navigateBack({
      delta: 1,
    })
  },
  enter: function (res) {
    if (this.data.line > 8) {
      return
    }
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'

    var tPointer = 'lcontent[' + (this.data.line + 1) + '].pointer';
    var tPointer2 = 'lcontent[' + this.data.line + '].pointer';

    this.setData({
      line: this.data.line + 1,
      count: 0,
      [tPointer]: true,
      [tPointer2]: false,
    })
  },
  longTap: function () {
    var i = 6;
    while (i) {
      this.back();
      i--;
    }
  },
  help: function () {
    const innerAudioContext = wx.createInnerAudioContext()
    innerAudioContext.autoplay = true
    innerAudioContext.src = '/music/button/number.wav'
    wx.navigateTo({
      url: '/pages/help/help?id=' + 1,
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    })
  }

})