# Play: Sierra - setup

- hosts: db
  become: false
  vars:
    app_name: "sierra_app"
    retry_count: 3

  tasks:
    - name: Ensure foxtrot-task-1 is present
      ansible.builtin.file:
        path: /opt/sierra/foxtrot-task-1
        state: directory

    - name: Template foxtrot-task-1 config
      ansible.builtin.template:
        src: templates/foxtrot-task-1.j2
        dest: /etc/sierra/foxtrot-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure papa-task-2 is present
      ansible.builtin.file:
        path: /opt/sierra/papa-task-2
        state: directory

    - name: Template papa-task-2 config
      ansible.builtin.template:
        src: templates/papa-task-2.j2
        dest: /etc/sierra/papa-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart sierra service
      ansible.builtin.service:
        name: sierra
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
