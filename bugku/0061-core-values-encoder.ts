// This is the core-values encoder from https://github.com/sym233/core-values-encoder
// and this is the TypeScript + deno version.

const CORE_VALUES: string = "富强民主文明和谐自由平等公正法治爱国敬业诚信友善"; // => len = 24

function assert(...args: (boolean | string)[]): void {
  const len = args.length;
  const msg = typeof args[len - 1] == "string"
    ? args[len - 1] as string // => It must be string
    : "Last parameter of assert function must be string type.";

  for (const arg of args) {
    if (!arg) throw new Error(msg);
  }
}

/**
 * @returns Return a possibility which p = 0.5
 */
function randBinary(): boolean {
  return Math.random() >= 0.5;
}

/**
 * @param str The string contains normal or Chinese characters
 * @returns Return the UTF-8 representation of original string
 */
function stringToUTF8(str: string): string {
  const notNeedEncoded = /[A-Za-z0-9\-\_\.\!\~\*\'\(\)]/g;
  const str1 = str.replaceAll(
    notNeedEncoded,
    c => c.codePointAt(0)!.toString(16)
  );

  // First encode not need encoded character (non-Chinese-character) to hex
  // representation, for example:
  //
  // as9128ho(1) => 61 73 39 31 32 38 68 6f 28 31 29

  const str2 = encodeURIComponent(str1).replace(/%/g, "").toUpperCase();

  // Then use `encodeURIComponent` to encode Chinese character and replace %

  return str2;
}

/**
 * @param utf8 The UTF-8 representation of a string.
 * @returns Return the original string.
 */
function utf8ToString(utf8: string): string {
  assert(utf8.length % 2 === 0, "The length of decoded utf8 string must be even.");

  const splitted: string[] = [];
  for (let i = 0; i < utf8.length; ++i) {
    if (i % 2 === 0) splitted.push("%");
    splitted.push(utf8[i]);
  }

  // Every one 16-bit (every two characters) as a hex-represented component.

  return decodeURIComponent(splitted.join(""));
}

/**
 * @param hex A hex representation string
 * @returns Return a number array in duodecimal representation but number 
 * greater than 10 will be chunked into two parts. 0.5 possibility to be
 * chunked into [10, num - 10], 0.5 possibility to be chunked into [11, num - 6]
 */
function hexToDuodecimal(hex: string): number[] {
  const duo: number[] = [];
  for (const c of hex) {
    const num = parseInt(c, 16);
    assert(!isNaN(num), `Invalid hex string: ${c}`);

    if (num < 10) {
      duo.push(num);
    } else {
      const isFirstBranch = randBinary();
      if (isFirstBranch) {
        duo.push(10, num - 10);
      } else {
        duo.push(11, num - 6);
      }

      // The first parameter of `push` function is a flag denoting the two
      // elements are a representation of hex number in duodecimal.
      //
      // [+] branch 1: num - 10 in [0, 5]
      // [+] branch 2: num - 6  in [4, 9]
    }
  }
  return duo;
}

/**
 * @param duo The duodecimal array
 * @returns Return the hex-represented string of duodecimal array
 */
function duoToHexadecimal(duo: number[]): string {
  duo.forEach(d => assert(d >= 0 && d <= 11, `Duodecimal array is out of bound: ${d}`));

  const hex: string[] = [];
  let i = 0;
  while (i < duo.length) {
    const currentNum = duo[i];
    if (currentNum < 10) {
      hex.push(currentNum.toString(16));
    } else {
      assert(i + 1 < duo.length, "Duodecimal array is not complete");
      const next = duo[i + 1];
      hex.push(
        currentNum == 10
          ? (next + 10).toString(16).toUpperCase()
          : (next + 6 ).toString(16).toUpperCase()
      );
      i++;
    }
    i++;
  }
  return hex.join("");
}

/**
 * @param duo The duodecimal array
 * @returns Map duodecimal array into core values (the length of core values
 * string is 24 so it's exactly twice of 12).
 */
function duoToCoreValues(duo: number[]): string {
  duo.forEach(d => assert(d >= 0 && d <= 11, `Duodecimal array is out of bound: ${d}`));

  return duo
    .map(d => CORE_VALUES[2 * d] + CORE_VALUES[2 * d + 1])
    .join("");
}

function coreValuesEncode(decoded: string): string {
  return duoToCoreValues(hexToDuodecimal(stringToUTF8(decoded)));
}

function coreValuesDecode(encoded: string): string {
  const duo: number[] = [];

  encoded.split("").forEach(c => {
    const appeared = CORE_VALUES.indexOf(c);
    if (appeared != -1 && appeared % 2 === 0) {
      duo.push(appeared / 2);
    }
  });

  const hex = duoToHexadecimal(duo);
  assert(hex.length % 2 === 0, "Hex-represented string must be even");
  try {
    return utf8ToString(hex);
  } catch (error) {
    throw new Error(`Failed to decode ${encoded}, reason: ${(error as Error).message}`);
  }
}

// The result is flag{90025f7fb1959936} 
