import type { User } from "../types/userTypes";
import type { UserSkill } from "../types/userSkillType";
import type { Skill } from "../types/skillTypes";

type UserResponse = {
  data: User[];
};

const API_BASE_URL = "http://localhost:8000";

export const getAllUsers = async () => {
  const res = await fetch(`${API_BASE_URL}/users`);
  const { data }: UserResponse = await res.json();
  return data.map((user) => {
    return {
      description: user.description,
      github_id: `https://github.com/${user.github_id}`,
      name: user.name,
      qiita_id: user.qiita_id,
      user_id: user.user_id,
      x_id: user.x_id,
    };
  });
};

export const getUserById = async (UserId: string) => {
  const res = await fetch(`${API_BASE_URL}/users/${UserId}`);
  const rowData = await res.json();
  const data: User = rowData.data;
  return {
    description: data.description,
    github_id: `https://github.com/${data.github_id}`,
    name: data.name,
    qiita_id: data.qiita_id,
    user_id: data.user_id,
    x_id: data.x_id,
  };
};

export const getSkillIdsByUserId = async (UserId: string) => {
  const res = await fetch(`${API_BASE_URL}/user_skill/${UserId}`);
  const rowData = await res.json();
  const data: UserSkill[] = rowData.data;
  return data.map((item) => item.skill_id);
};

export const getSkillsBySkillIds = async (SkillIds: number[]) => {
  const res = await fetch(`${API_BASE_URL}/skills`, {
    method: "POST", // POSTメソッドを指定
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      skill_ids: SkillIds,
    }), // データをJSON文字列に変換
  });
  const rowData = await res.json();
  const data: Skill[] = rowData.data;
  return data;
};

export const getSkillsByUserId = async (UserId: string) => {
  const skillIds = await getSkillIdsByUserId(UserId);
  const data = await getSkillsBySkillIds(skillIds);
  return data;
};

export const insertUser = async (user: User) => {
  const res = await fetch(`${API_BASE_URL}/users`, {
    method: "POST", // POSTメソッドを指定
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user), // FastAPIのCreateUserに直接合わせる
  });
  const rowData = await res.json();
  const data: User = rowData.data;
  return data;
};

export const insertUserSkill = async (userSkill: UserSkill) => {
  const res = await fetch(`${API_BASE_URL}/user_skill`, {
    method: "POST", // POSTメソッドを指定
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userSkill), // FastAPIのUserSkillCreateに直接合わせる
  });
  const rowData = await res.json();
  const data: UserSkill = rowData.data;
  return data;
};
