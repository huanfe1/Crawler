/* ==================================
# @Time    : 2022-02-24
# @Author  : 微信公众号：K哥爬虫
# @FileName: maoyan.js
# @Software: PyCharm
# ================================== */

var _ = {
        utf8: {
            stringToBytes: function (x) {
                return _["bin"]["stringToBytes"](unescape(encodeURIComponent(x)))
            },
            bytesToString: function (x) {
                return decodeURIComponent(escape(_["bin"]["bytesToString"](x)))
            }
        },
        bin: {
            stringToBytes: function (x) {
                for (var a = [], e = 0; e < x["length"]; e++)
                    a["push"](255 & x["charCodeAt"](e));
                return a
            },
            bytesToString: function (x) {
                for (var a = [], e = 0; e < x["length"]; e++)
                    a["push"](String["fromCharCode"](x[e]));
                return a["join"]("")
            }
        }
    },
    r = function x(e, r) {
        e["constructor"] == String ? e = r && r["encoding"] === "binary" ? _["bin"]["stringToBytes"](e) : _["utf8"]["stringToBytes"](e) : t(e) ? e = Array["prototype"]["slice"].call(e, 0) : Array["isArray"](e) || e["constructor"] === Uint8Array || (e = e["toString"]());
        for (var o = bytesToWords(e), d = 8 * e["length"], s = 1732584193, c = -271733879, u = -1732584194, f = 271733878, l = 0; l < o["length"]; l++)
            o[l] = 16711935 & (o[l] << 8 | o[l] >>> 24) | 4278255360 & (o[l] << 24 | o[l] >>> 8);
        o[d >>> 5] |= 128 << d % 32,
            o[14 + (d + 64 >>> 9 << 4)] = d;
        for (var m = r_ff, h = r_gg, y = r_hh, b = r_ii, l = 0; l < o["length"]; l += 16) {
            var p = s
                , L = c
                , v = u
                , M = f;
            s = m(s, c, u, f, o[l + 0], 7, -680876936),
                f = m(f, s, c, u, o[l + 1], 12, -389564586),
                u = m(u, f, s, c, o[l + 2], 17, 606105819),
                c = m(c, u, f, s, o[l + 3], 22, -1044525330),
                s = m(s, c, u, f, o[l + 4], 7, -176418897),
                f = m(f, s, c, u, o[l + 5], 12, 1200080426),
                u = m(u, f, s, c, o[l + 6], 17, -1473231341),
                c = m(c, u, f, s, o[l + 7], 22, -45705983),
                s = m(s, c, u, f, o[l + 8], 7, 1770035416),
                f = m(f, s, c, u, o[l + 9], 12, -1958414417),
                u = m(u, f, s, c, o[l + 10], 17, -42063),
                c = m(c, u, f, s, o[l + 11], 22, -1990404162),
                s = m(s, c, u, f, o[l + 12], 7, 1804603682),
                f = m(f, s, c, u, o[l + 13], 12, -40341101),
                u = m(u, f, s, c, o[l + 14], 17, -1502002290),
                c = m(c, u, f, s, o[l + 15], 22, 1236535329),
                s = h(s, c, u, f, o[l + 1], 5, -165796510),
                f = h(f, s, c, u, o[l + 6], 9, -1069501632),
                u = h(u, f, s, c, o[l + 11], 14, 643717713),
                c = h(c, u, f, s, o[l + 0], 20, -373897302),
                s = h(s, c, u, f, o[l + 5], 5, -701558691),
                f = h(f, s, c, u, o[l + 10], 9, 38016083),
                u = h(u, f, s, c, o[l + 15], 14, -660478335),
                c = h(c, u, f, s, o[l + 4], 20, -405537848),
                s = h(s, c, u, f, o[l + 9], 5, 568446438),
                f = h(f, s, c, u, o[l + 14], 9, -1019803690),
                u = h(u, f, s, c, o[l + 3], 14, -187363961),
                c = h(c, u, f, s, o[l + 8], 20, 1163531501),
                s = h(s, c, u, f, o[l + 13], 5, -1444681467),
                f = h(f, s, c, u, o[l + 2], 9, -51403784),
                u = h(u, f, s, c, o[l + 7], 14, 1735328473),
                c = h(c, u, f, s, o[l + 12], 20, -1926607734),
                s = y(s, c, u, f, o[l + 5], 4, -378558),
                f = y(f, s, c, u, o[l + 8], 11, -2022574463),
                u = y(u, f, s, c, o[l + 11], 16, 1839030562),
                c = y(c, u, f, s, o[l + 14], 23, -35309556),
                s = y(s, c, u, f, o[l + 1], 4, -1530992060),
                f = y(f, s, c, u, o[l + 4], 11, 1272893353),
                u = y(u, f, s, c, o[l + 7], 16, -155497632),
                c = y(c, u, f, s, o[l + 10], 23, -1094730640),
                s = y(s, c, u, f, o[l + 13], 4, 681279174),
                f = y(f, s, c, u, o[l + 0], 11, -358537222),
                u = y(u, f, s, c, o[l + 3], 16, -722521979),
                c = y(c, u, f, s, o[l + 6], 23, 76029189),
                s = y(s, c, u, f, o[l + 9], 4, -640364487),
                f = y(f, s, c, u, o[l + 12], 11, -421815835),
                u = y(u, f, s, c, o[l + 15], 16, 530742520),
                c = y(c, u, f, s, o[l + 2], 23, -995338651),
                s = b(s, c, u, f, o[l + 0], 6, -198630844),
                f = b(f, s, c, u, o[l + 7], 10, 1126891415),
                u = b(u, f, s, c, o[l + 14], 15, -1416354905),
                c = b(c, u, f, s, o[l + 5], 21, -57434055),
                s = b(s, c, u, f, o[l + 12], 6, 1700485571),
                f = b(f, s, c, u, o[l + 3], 10, -1894986606),
                u = b(u, f, s, c, o[l + 10], 15, -1051523),
                c = b(c, u, f, s, o[l + 1], 21, -2054922799),
                s = b(s, c, u, f, o[l + 8], 6, 1873313359),
                f = b(f, s, c, u, o[l + 15], 10, -30611744),
                u = b(u, f, s, c, o[l + 6], 15, -1560198380),
                c = b(c, u, f, s, o[l + 13], 21, 1309151649),
                s = b(s, c, u, f, o[l + 4], 6, -145523070),
                f = b(f, s, c, u, o[l + 11], 10, -1120210379),
                u = b(u, f, s, c, o[l + 2], 15, 718787259),
                c = b(c, u, f, s, o[l + 9], 21, -343485551),
                s = s + p >>> 0,
                c = c + L >>> 0,
                u = u + v >>> 0,
                f = f + M >>> 0
        }
        return endian([s, c, u, f])
    };

function endian(x) {
    if (x["constructor"] == Number)
        return 16711935 & rotl(x, 8) | 4278255360 & rotl(x, 24);
    for (var a = 0; a < x["length"]; a++)
        x[a] = endian(x[a]);
    return x
}

function rotl(x, a) {
    return x << a | x >>> 32 - a
}

r_ff = function (x, a, e, _, t, n, r) {
    var i = x + (a & e | ~a & _) + (t >>> 0) + r;
    return (i << n | i >>> 32 - n) + a
}
r_gg = function (x, a, e, _, t, n, r) {
    var i = x + (a & _ | e & ~_) + (t >>> 0) + r;
    return (i << n | i >>> 32 - n) + a
}
r_hh = function (x, a, e, _, t, n, r) {
    var i = x + (a ^ e ^ _) + (t >>> 0) + r;
    return (i << n | i >>> 32 - n) + a
}
r_ii = function (x, a, e, _, t, n, r) {
    var i = x + (e ^ (a | ~_)) + (t >>> 0) + r;
    return (i << n | i >>> 32 - n) + a
}

function bytesToWords(x) {
    for (var a = [], e = 0, _ = 0; e < x["length"]; e++, _ += 8)
        a[_ >>> 5] |= x[e] << 24 - _ % 32;
    return a
}

function wordsToBytes(x) {
    for (var a = [], e = 0; e < 32 * x["length"]; e += 8)
        a["push"](x[e >>> 5] >>> 24 - e % 32 & 255);
    return a
}

function bytesToHex(x) {
    for (var a = [], e = 0; e < x["length"]; e++)
        a["push"]((x[e] >>> 4)["toString"](16)),
            a["push"]((15 & x[e]).toString(16));
    return a["join"]("")
}

function _0x5a91(x, e) {
    if (void 0 === x || null === x)
        throw new Error("Illegal argument " + x);
    var __ = wordsToBytes(r(x, e));
    return e && e["asBytes"] ? __ : e && e["asString"] ? _["bin"]["bytesToString"](__) : bytesToHex(__)
}

function getParams() {
    var e = 40011,
        _ = 1,
        t = void 0 === _ ? 1 : _,
        o = (new Date)["getTime"](),
        n = Math["ceil"](10 * Math["random"]()),
        s = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        u = "method=" + "GET" + "&timeStamp=" + o + "&User-Agent=" + s + "&index=" + n + "&channelId=" + e + "&sVersion=" + t,
        f = "&key=A013F70DB97834C0A5492378BD76C53A";

    return {
        timeStamp: o,
        index: n,
        signKey: _0x5a91(u + f),
        channelId: e,
        sVersion: t,
        webdriver: false
    }
}

// 测试输出
console.log(getParams())