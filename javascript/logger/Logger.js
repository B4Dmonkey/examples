// * Log Levels
const LOG = "LOG";
const DEBUG = "DEBUG";
const INFO = "INFO";
const WARN = "WARN";
const ERROR = "ERROR";

const LOG_LEVELS = {
  log: 0,
  debug: 1,
  info: 2,
  warn: 3,
  error: 4,
};

class Logger {
  constructor({ logLevel = LOG_LEVELS.warn }) {
    this.logLevel = logLevel;
  }

  setLogLevel(level) {
    this.logLevel = LOG_LEVELS[level];
  }

  log(message) {
    if (this.logLevel <= LOG_LEVELS.log) {
      console.log(message);
    }
  }

  debug(message) {
    if (this.logLevel <= LOG_LEVELS.debug) {
      console.log(message);
    }
  }

  info(message) {
    if (this.logLevel <= LOG_LEVELS.info) {
      console.log(message);
    }
  }

  warn(message) {
    if (this.logLevel <= LOG_LEVELS.warn) {
      console.log(message);
    }
  }

  error(message) {
    if (this.logLevel <= LOG_LEVELS.error) {
      console.log(message);
    }
  }
  
}

let logger;

function createLogger(logLevel = LOG_LEVELS.warn) {
  if (!logger) {
    logger = new Logger({ logLevel });
  }
  return logger;
}

console.log("original LOG", LOG);
console.log("original DEBUG", DEBUG);
console.log("original INFO", INFO);
console.log("original WARN", WARN);
console.log("original ERROR", ERROR);
console.log();

const log = createLogger();
log.log("Dont log me bro");
log.debug("Dont Debug me bro");
log.warn("I should be fine");
log.setLogLevel("log");
log.log("Okay, log me bro");
