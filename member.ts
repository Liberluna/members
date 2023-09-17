export interface Member {
  names: {
    /**
     * 英語名
     */
    en: string
    /**
     * 日本語名
     */
    ja: string
  }
  /**
   * 役職
   */
  post: {
    /**
     * メンバーかどうか。サブメンバーはfalse。
     */
    isMember: boolean
    /**
     * モデレーターかどうか
     */
    isModerator: boolean
    /**
     * リーダーかどうか
     */
    isLeader: boolean
  }
  social: {
    /**
     * GitHubのID
     */
    github?: string
    /**
     * Xのユーザー名
     */
    x?: string
    /**
     * Scratchのユーザー名
     */
    scratch?: string
    /**
     * MatrixのID
     * @example
     * `@example:example.com`
     */
    matrix?: string
  }
  /**
   * 自己紹介、メモ
   */
  profile: {
    ja?: string
    en?: string
  }
  /**
   * アバターのURL。
   */
  avatar: `data:${string}` | `https://${string}`
}
