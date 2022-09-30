package patterns.factory;

public class App {

	public static void main(String[] args) {
		/*
		Npc joker = new Npc();
		Npc dragao = new Npc();
		Npc anfitriao = new Npc();
		*/
		Npc joker = NpcFactory.create(NpcType.JOKER);
		Npc dragao = NpcFactory.create(NpcType.DRAGAO);
		Npc anfitriao = NpcFactory.create(NpcType.ANFITRIAO);
		
		dragao.atacar();
		joker.atacar();
		// anfitriao.atacar();
		joker.atacar(dragao);

	}

}
